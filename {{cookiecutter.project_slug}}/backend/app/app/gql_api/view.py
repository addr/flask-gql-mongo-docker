from flask_graphql import GraphQLView
from .schema import schema


def gql_view():
    return GraphQLView.as_view('graphql', schema=schema, graphiql=True)
