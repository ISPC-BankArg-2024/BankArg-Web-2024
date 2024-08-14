import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { LoginComponent } from 'src/app/vistas/login/login.component';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  public currentUserLoginOn = new BehaviorSubject<boolean>(false);
  constructor() {}


  login() {
    this.currentUserLoginOn.next(true);
    console.log('User logged in:', this.currentUserLoginOn.value);
  }

  logout() {
    this.currentUserLoginOn.next(false);
    console.log('User logged out:', this.currentUserLoginOn.value)
  }

  getIsAuthenticated():boolean {
    console.log('Authenticated:', this.currentUserLoginOn);
    return this.currentUserLoginOn.value;
  }

  loginStatus() {
    this.currentUserLoginOn.next(true);
    console.log(this.currentUserLoginOn);
  }

  get userLoginOn(): Observable<boolean> {
    return this.currentUserLoginOn.asObservable();
  }
}
