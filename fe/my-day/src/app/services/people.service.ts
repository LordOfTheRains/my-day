import { Injectable } from "@angular/core";
import { Apollo } from "apollo-angular";
import { Observable } from "rxjs";
import { map, tap } from "rxjs/operators";
import { GET_PEOPLE_WITH_OBLIGATIONS } from "./queries";
import { People, People_people } from "./__generated__/People";

@Injectable({ providedIn: "root" })
export class PeopleService {

  constructor (private apollo: Apollo) { }


  getPeople (opt: { withObligations: boolean; }): Observable<People_people[]> {
    return this.apollo.watchQuery<People>({ query: GET_PEOPLE_WITH_OBLIGATIONS }).valueChanges.pipe(
      map(result => result.data.people)
    );
  }
}