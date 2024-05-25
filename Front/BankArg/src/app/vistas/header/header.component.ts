import { Component, OnInit } from '@angular/core';
import { LoginComponent } from '../login/login.component';
import { LoginService } from 'src/app/servicios/auth/login.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
  
})
export class HeaderComponent {

  validacion = false;
  userLoginOn:boolean=this.loginService.currentUserLoginOn.value;

constructor (private loginService: LoginService){}

 ngOnInit():void{
   this.loginService.currentUserLoginOn.subscribe(
     {
       next:(userLoginOn) => {
         this.userLoginOn=userLoginOn;
       }
     }
     
   )
   console.log(this.userLoginOn);
   console.log(this.loginService.currentUserLoginOn);
   
 }

  public change() {
    if (this.validacion === true){
     this.validacion = false
  }
    else{
      this.validacion = true
  }

}
}
