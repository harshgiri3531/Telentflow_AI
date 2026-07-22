const API_BASE = "http://127.0.0.1:8000/api";

function getToken() {
    return localStorage.getItem("access_token");
}

function saveTokens(access, refresh) {
    localStorage.setItem("access_token", access);
    localStorage.setItem("refresh_token", refresh);
}

function logout() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    window.location.href = "/login/";
}

async function apiRequest(endpoint, method = "GET", body = null) {
    const headers = { "Content-Type": "application/json" };
    const token = getToken();
    if (token) headers["Authorization"] = "Bearer " + token;

    const res = await fetch(API_BASE + endpoint, {
        method,
        headers,
        body: body ? JSON.stringify(body) : null,
    });

    if (res.status === 401) {
        logout();
        return null;
    }
    return res;
}