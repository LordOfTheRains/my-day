/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.


// ====================================================
// GraphQL query operation: Chores
// ====================================================


export interface Chores_chores {
  __typename: "ChoreObject";
  name: string;
  description: string | null;
  duration: number;
}

export interface Chores {
  chores: (Chores_chores | null)[] | null;
}
