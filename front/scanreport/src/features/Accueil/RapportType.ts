export interface AdresseIp {
    id: number;
    ip_address: string;
    status: boolean;
}

export interface Rapport {
    id: number;
    name: string;
    type: string;
    file_path: string;
    format: string;
    created_at: string;
}