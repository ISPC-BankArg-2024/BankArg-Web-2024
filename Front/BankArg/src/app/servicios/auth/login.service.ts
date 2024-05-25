import { Injectable } from '@angular/core';
import { BehaviorSubject,Observable } from 'rxjs';
import { LoginComponent } from 'src/app/vistas/login/login.component';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  currentUserLoginOn: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  constructor() { }

loginStatus(){
  this.currentUserLoginOn.next(true);
  console.log(this.currentUserLoginOn);
}



  get userLoginOn(): Observable<boolean>{
    return this.currentUserLoginOn.asObservable();
  }
}
