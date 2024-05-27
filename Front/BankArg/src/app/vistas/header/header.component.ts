import { Component, OnInit } from '@angular/core';
import { LoginComponent } from '../login/login.component';
import { LoginService } from 'src/app/servicios/auth/login.service';
import Swal from 'sweetalert2';

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
   
 }
 logout(){
  this.loginService.currentUserLoginOn.next(false);
  console.log (this.userLoginOn);
  Swal.fire({
    title: 'Deslogueo Exitoso',
    text: 'El usuario se ha deslogueado correctamente',
    icon: 'info',
    showConfirmButton: true,
    confirmButtonText: 'Aceptar',
  })
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
