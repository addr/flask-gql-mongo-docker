import buildGraphqlProvider, { buildQuery } from "ra-data-graphql-simple";
import gql from "graphql-tag";
import { ApolloLink } from "apollo-link";
import { HttpLink } from "apollo-link-http";

const myBuildQuery = introspection => (fetchType, resource, params) => {
  const builtQuery = buildQuery(introspection)(fetchType, resource, params);

  /*
   * Query customization goes here
   */

  return builtQuery;
};

const httpLink = new HttpLink({
  uri: "/graphql"
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

export default () =>
  buildGraphqlProvider({
    buildQuery: myBuildQuery,
    clientOptions: {
      link: authLink.concat(httpLink)
    }
  });
