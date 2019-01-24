import gql from "graphql-tag";
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { ApolloLink } from "apollo-link";
import { InMemoryCache } from "apollo-cache-inmemory";

const host = "/graphql";
const httpLink = new HttpLink({
  uri: host
});
const authLink = new ApolloLink((operation, forward) => {
  // Retrieve the authorization token from local storage.
  const token = localStorage.getItem("token");

  // Use the setContext method to set the HTTP headers.
  operation.setContext({
    headers: {
      Authorization: token ? `Bearer ${token}` : ""
    }
  });

  // Call the next link in the middleware chain.
  return forward(operation);
});

const cache = new InMemoryCache();
const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache
});

export async function login(email, password) {
  const authResult = await client.mutate({
    mutation: gql`
      mutation login($email: String!, $password: String!) {
        login(password: $password, email: $email) {
          token
          user {
            roles {
              edges {
                node {
                  name
                }
              }
            }
          }
        }
      }
    `,
    variables: {
      email: email,
      password: password
    }
  });
  const { token } = authResult.data.login;
  const { edges } = authResult.data.login.user.roles;
  const roleNames = edges.map(edge => edge.node.name);
  const { errors } = authResult;
  if (errors) {
    return Promise.reject();
  } else {
    localStorage.setItem("email", email);
    localStorage.setItem("token", token);
    localStorage.setItem("roles", roleNames);
    return Promise.resolve();
  }
}

export async function logout(token) {
  const logoutResult = await client.mutate({
    mutation: gql`
      mutation logout {
        logout {
          status
        }
      }
    `
  });
  const { errors } = logoutResult;

  if (errors) {
    return Promise.reject();
  } else {
    return Promise.resolve();
  }
}
