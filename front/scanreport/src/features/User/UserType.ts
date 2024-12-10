export interface User {
    id: number;
    firstname: string;
    lastname: string;
    email: string;
    role: string;
}

export interface CurrentUser {
    id: number;
    firstname: string;
    lastname: string;
    email: string;
    token: string;
    role: string;
}