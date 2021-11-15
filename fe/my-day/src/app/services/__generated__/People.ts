/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.


import { ObligationType } from "./../../../../__generated__/globalTypes";

// ====================================================
// GraphQL query operation: People
// ====================================================


export interface People_people_obligations_EventObject {
  __typename: "EventObject";
  description: string | null;
  name: string;
  obligationType: ObligationType | null;
}

export interface People_people_obligations_ChoreObject {
  __typename: "ChoreObject";
  name: string;
  description: string | null;
  obligationType: ObligationType | null;
  duration: number;
}

export type People_people_obligations = People_people_obligations_EventObject | People_people_obligations_ChoreObject;

export interface People_people {
  __typename: "PersonObject";
  name: string;
  obligations: (People_people_obligations | null)[];
}

export interface People {
  people: (People_people | null)[] | null;
}
