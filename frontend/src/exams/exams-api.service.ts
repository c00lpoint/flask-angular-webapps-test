import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import { catchError } from 'rxjs/operators';
import {API_URL} from '../app/env';
import {Exam} from './exam.model';

@Injectable()
export class ExamsApiService{
	constructor(private http: HttpClient){
	}

	private static _handleError(err: HttpErrorResponse | any){
		return Observable.throw(err.message || 'Error: Unable to complete request.');
	}

	// Get list of public, future events
	getExams(): Observable<any>{
		return this.http
		.get(`${API_URL}/exams`)
		.pipe(catchError(ExamsApiService._handleError))
	}
}