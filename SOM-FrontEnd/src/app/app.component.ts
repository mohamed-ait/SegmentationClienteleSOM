import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  inputData : any;
  constructor(private http: HttpClient) {
  }
uploadFile(file: File) {
  const formData = new FormData();
  formData.append('file', file);

  return this.http.post('http://localhost:8085/upload', formData);
}
 onSubmit(){
    console.log( this.inputData);
    this.uploadFile(this.inputData);
 }
}
