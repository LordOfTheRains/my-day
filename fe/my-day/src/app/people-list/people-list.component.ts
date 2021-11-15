import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { PeopleService } from '../services/people.service';
import { People_people } from '../services/__generated__/People';

@Component({
  selector: 'app-people-list',
  templateUrl: './people-list.component.html',
  styleUrls: ['./people-list.component.scss']
})
export class PeopleListComponent implements OnInit {


  people$: Observable<People_people[]>;

  constructor (
    private peopleService: PeopleService
  ) {

  }

  ngOnInit (): void {
    this.people$ = this.peopleService.getPeople({ withObligations: false });
  }

}
