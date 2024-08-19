import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { response } from 'express';
import { ApiService } from 'src/app/servicios/api/api.service';

import Swal from 'sweetalert2';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css'],
})
export class PerfilComponent {

user: any;

ngOnInit(){
  this.user = {
    name: '',
    lastname: '',
    email: '',
    id: ''
  }

  this.cuenta.userDetails();
}

  constructor(private router: Router, private cuenta: ApiService) {

    this.cuenta.userDetails().subscribe(data =>{
    this.user.name= data.name;
    this.user.lastname= data.lastname;
    this.user.email= data.email;
    this.user.id= data.id;


    })

  }




  editarButton() {
    Swal.fire({
      title: 'Editar perfil',
      text: '¿Desea editar su perfil?',
      icon: 'info',
      showConfirmButton: true,
      confirmButtonText: 'Aceptar',
      showCancelButton: true,
      cancelButtonText: 'Cancelar',
    }).then((value) => {
      if (value.isConfirmed) {
        Swal.fire({
          title: 'Ok',
          text: 'Sera redirigido a la pagina para editar perfiles',
          icon: 'success',
          showConfirmButton: true,
          confirmButtonText: 'Aceptar',
        }).then(() => {
          this.router.navigate(['/personas']);

          // window.location.href = '../personas';
        });
        // Swal.fire({
        //     title: "Error",
        //     text: "Usted no tiene permisos para editar su perfil",
        //     icon: "error",
        //     showConfirmButton:true,
        //     confirmButtonText: 'Aceptar'
        //         });
        //         // window.location.href = "./editarPerfil.html";
      } else if (value.dismiss) {
        Swal.fire({
          title: 'Edición cancelada',
          text: 'La edición del perfil ha sido cancelada',
          icon: 'info',
          showConfirmButton: true,
          confirmButtonText: 'Aceptar',
        });
      }
    });
  }
}
