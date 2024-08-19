import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { Title } from '@angular/platform-browser';
import Swal from 'sweetalert2';
import { Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/servicios/api/api.service';
import { BehaviorSubject, Observable, tap } from 'rxjs';
// import { LoginService } from 'src/app/servicios/auth/login.service';
import { LoginService } from 'src/app/servicios/auth/login.service';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  login: any;

  // TODO
  ngOnInit() {
    this.login = {
      email: '',
      password: '',
    };
  }

  constructor(
    private formBuilder: FormBuilder,
    private cuenta: ApiService,
    private router: Router,
    private loginService: LoginService
  ) {
    //Creamos el grupo de controles para el formulario
    this.form = this.formBuilder.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]],
    });
  }

  get username() {
    return this.form.get('username');
  }

  get password() {
    return this.form.get('password');
  }

  // users: { [key: string]: string } = {
  //   admin: 'admin',
  //   user: 'user',
  //   guest: 'guest',
  //   Eze: '1234',
  //   Yo: '5678',
  //   'juanPerez@gmail.com': '1234',
  //   'admin@mail.com': '1234',
  // };

  btnLogin = document.getElementById('btnLogin');

  iniciarSesion() {
    let user = this.username?.value;
    let pass = this.password?.value;
    if (user === '' || pass === '') {
      Swal.fire({
        title: 'Error',
        text: 'Debe ingresar usuario y contraseña',
        icon: 'error',
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
      });
    } else {
      // TODO


      this.cuenta.login(this.login).subscribe({
        next:(token)=>{
          sessionStorage.setItem('token', token.token);
          console.log(token);
          Swal.fire({
            title: 'Login exitoso',
            text: 'El usuario se ha logueado correctamente',
            icon: 'success',
            showConfirmButton: true,
            confirmButtonText: 'Aceptar',
          });
          this.loginService.loginStatus();
          this.router.navigate(['']);
        },
        error: (e:HttpErrorResponse) =>{
          Swal.fire({
            title: `Error status ${e.status}`,
            text: 'El usuario o contraseña son incorrectos',
            icon: 'error',
            showConfirmButton: true,
            confirmButtonText: 'Aceptar',
          });
        }
        
      });
     // this.cuenta.login(this.login).subscribe(
     //   (res) => {
     //     (token: string) => {
     //       localStorage.setItem('token', token);
     //       console.log('token');
     //       
     //     }
         
    //      //this.currentUserLoginOn.next(true);
    //      Swal.fire({
    //        title: 'Login exitoso',
    //        text: 'El usuario se ha logueado correctamente',
    //        icon: 'success',
    //        showConfirmButton: true,
    //        confirmButtonText: 'Aceptar',
    //      }).then(() => {
    //        this.loginService.loginStatus();
    //        this.router.navigate(['']);
    //        // window.location.href = '../body/home';
    //      });
    //    
    //    (err: any) => {
    //      console.log(err);
    //      Swal.fire({
    //        title: 'Error',
    //        text: 'El usuario o contraseña son incorrectos',
    //        icon: 'error',
    //        showConfirmButton: true,
    //        confirmButtonText: 'Aceptar',
    //      });
    //    }
    //  }
    //  ;
      // if (this.users[user] === pass) {

      //   Swal.fire({
      //     title: 'Login exitoso',
      //     text: 'El usuario se ha logueado correctamente',
      //     icon: 'success',
      //     showConfirmButton: true,
      //     confirmButtonText: 'Aceptar',
      //   }).then(function () {
      //     window.location.href = '../index.html';
      //   });
      // } else {
      //   Swal.fire({
      //     title: 'Error',
      //     text: 'El usuario o contraseña son incorrectos',
      //     icon: 'error',
      //     showConfirmButton: true,
      //     confirmButtonText: 'Aceptar',
      //   });
      // }
    }
  }
}
