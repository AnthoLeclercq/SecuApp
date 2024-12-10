export function roleLibelle(role: string) {
    if (role === "ROLE_ADMIN") {
        return "Administrator"
    } else if (role === "ROLE_USER") {
        return "User"
    }
    return "";
}


export function convertDate(date: Date) {
    date = new Date(date)
    return date.toLocaleDateString();
}
