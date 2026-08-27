const API_BASE = window.location.origin + "/api";

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

async function loadNotifications() {
    const res = await apiRequest("/notifications/");
    if (!res) return;
    const data = await res.json();
    const badge = document.getElementById("notif-badge");
    if (data.length > 0) {
        badge.textContent = data.length;
        badge.classList.remove("d-none");
    }
    const list = document.getElementById("notif-list");
    list.innerHTML = data.map(n => `<li class="list-group-item">${n.message}</li>`).join("") || "<li class='list-group-item text-muted'>No notifications</li>";
}

function toggleNotifications() {
    document.getElementById("notif-dropdown").classList.toggle("d-none");
}