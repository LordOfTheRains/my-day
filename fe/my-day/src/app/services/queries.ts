import gql from "graphql-tag";

export const GET_PEOPLE_WITH_OBLIGATIONS = gql`
query People {
  people {
    name
    obligations {
      ... on EventObject {
        description
        name
        obligationType
      }
      
      ... on ChoreObject {
        name
        description
        obligationType
        duration
      }
    }
  }
}
`;


export const GET_EVENTS = gql`
query Events{
  events {
    name
    description
  }
}
`


export const GET_CHORES = gql`
query Chores{
  chores {
    name
    description
    duration
  }
}
`