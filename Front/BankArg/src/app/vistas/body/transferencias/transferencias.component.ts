import { Component } from '@angular/core';
import Swal from 'sweetalert2';
import { TransferirService } from 'src/app/servicios/services/transferir.service';
import { Persona } from 'src/app/modelos/persona';
import { ApiService } from 'src/app/servicios/api/api.service';
import { Router } from '@angular/router';
import { TransferenciasListaComponent } from '../transferencias-lista/transferencias-lista.component';

@Component({
  selector: 'app-transferencias',
  templateUrl: './transferencias.component.html',
  styleUrls: ['./transferencias.component.css'],
})
export class TransferenciasComponent {
  constructor(
    public transferirS: TransferirService,
    private cuenta: ApiService,
    private router: Router
  ) {}

  transferencias: any = this.cuenta.getTransferencias();
  transferenciasGral: any = this.cuenta.getTransferenciasGral();
  

  persona1 = new Persona(1, 'admin', 10000.5, 'admin', '10101010');

  persona2 = new Persona(2, 'joaquin', 8600, 'joacobonvechi', '20202020');

  persona3 = new Persona(3, 'ezequiel', 5900.6, 'ezegiampaoli', '30303030');

  contactos: Array<Persona> = [this.persona2, this.persona3];

  formateador = new Intl.NumberFormat('en');

  saldoformateado = this.formateador.format(this.persona1.saldo);

  public async Transferir() {
    const { value: destinatario } = await Swal.fire({
      title: 'Transferir',
      text: 'Ingresa el CBU del destinatario',
      input: 'text',
      inputValue: '',
    });

    for (let contacto of this.contactos) {
      if (contacto.cbu === destinatario) {
        var destinatarioPersona = contacto;

        const { value: monto } = await Swal.fire({
          title: 'Monto',
          text: 'Ingresa el monto a transferir a ' + destinatarioPersona.nombre,
          input: 'number',
          inputValue: '',
        });
        if (monto > this.persona1.saldo) {
          Swal.fire({
            title: 'Error',
            text: 'El monto supera su saldo',
            icon: 'error',
            showConfirmButton: true,
            confirmButtonText: 'Aceptar',
          });
        } else {
          this.transferirS.TransferirMontoAPersona(
            parseFloat(monto),
            this.persona1,
            destinatarioPersona
          );
          Swal.fire({
            title: 'Enviado',
            text: 'Tranferencia enviada',
            icon: 'success',
            showConfirmButton: true,
            confirmButtonText: 'Aceptar',
          });
        }
        this.saldoformateado = this.formateador.format(this.persona1.saldo);
        break;
      } else {
        Swal.fire({
          title: 'Error',
          text: 'No se encontro',
          icon: 'error',
          showConfirmButton: true,
          confirmButtonText: 'Aceptar',
        });
      }
    }
  }

  public AgregarContacto() {
    Swal.fire({
      title: 'Error',
      text: 'Usted no tiene permisos para agregar contactos',
      icon: 'error',
      showConfirmButton: true,
      confirmButtonText: 'Aceptar',
    });
  }

  public Historial() {
    // Swal.fire({
    //       title: "Error",
    //       text: "Usted no tiene permisos para ver el historial",
    //       icon: "error",
    //       showConfirmButton:true,
    //       confirmButtonText:"Aceptar"
    // })

    Swal.fire({
      title: 'Ok',
      text: 'Sera redirigido a la pagina para editar perfiles',
      icon: 'success',
      showConfirmButton: true,
      confirmButtonText: 'Aceptar',
    }).then(() => {
      this.router.navigate(['/transferenciasLista']);

      // window.location.href = '../personas';
    });

    this.cuenta.ObtenerUltimosMovimientos().subscribe((data: any) => {
      console.log(data);
      var movimientos = data;
      var movimientosFormateados = [];
      for (let movimiento of movimientos) {
        var movimientoFormateado =
          'Operacion: ' +
          movimiento.operacion +
          ' - ' +
          'Monto: ' +
          movimiento.monto +
          '';
        movimientosFormateados.push(movimientoFormateado);
      }
      Swal.fire({
        title: 'Historial',
        html: movimientosFormateados.join('<br>'),
        icon: 'info',
        showConfirmButton: true,
        confirmButtonText: 'Aceptar',
      });
    });
  }
}
