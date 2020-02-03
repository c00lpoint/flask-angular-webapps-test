export class Exam{
	constructor(
		public title: string,
		public description: string,
		public _id?: number,
		public createdAt?: Date,
		public updateAt?: Date,
		public lastUpdatedBy?: string
		){ }
	
}