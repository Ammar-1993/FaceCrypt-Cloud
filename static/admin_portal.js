// ============= Config =============
const API_BASE = 'http://127.0.0.1:8080';

// ============= Helpers =============
function show(elem) { elem.classList.remove('hidden'); }
function hide(elem) { elem.classList.add('hidden'); }
function setText(id, msg) { document.getElementById(id).innerHTML = msg; }

// ============= Admin Login =============
async function adminLogin() {
  const password = document.getElementById('adminPassword').value;
  const res = await fetch(`${API_BASE}/admin/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password })
  });
  const data = await res.json();
  if (res.ok) {
    setText('loginMessage', `<span class="text-success">✅ ${data.message}</span>`);
    hide(document.getElementById('loginSection'));
    show(document.getElementById('adminPanel'));
    await loadUsers();
    await fetchAuditLogs();
  } else {
    setText('loginMessage', `<span class="text-danger">❌ ${data.error}</span>`);
  }
}

// ============= Add User =============
async function addUser() {
  const userId = document.getElementById('newUserId').value;
  const name = document.getElementById('newUserName').value;
  const email = document.getElementById('newUserEmail').value;
  const image = document.getElementById('newUserImage').files[0];

  if (!userId || !name || !email || !image) {
    setText('addUserMessage', `<span class="text-danger">❌ Please fill all fields and choose an image.</span>`);
    return;
  }

  const formData = new FormData();
  formData.append('user_id', userId);
  formData.append('name', name);
  formData.append('email', email);
  formData.append('image', image);

  const res = await fetch(`${API_BASE}/admin/add_user`, { method: 'POST', body: formData });
  const data = await res.json();
  if (res.ok) {
    setText('addUserMessage', `<span class="text-success">✅ ${data.message}</span>`);
    await loadUsers();
  } else {
    setText('addUserMessage', `<span class="text-danger">❌ ${data.error}</span>`);
  }
}

// ============= Load Users for Deletion =============
async function loadUsers() {
  const select = document.getElementById('deleteUserId');
  select.innerHTML = '';
  const res = await fetch(`${API_BASE}/admin/list_users`);
  const data = await res.json();

  data.users.forEach(user => {
    const option = document.createElement('option');
    option.value = user.id;
    option.text = `${user.name} (${user.id})`;
    select.add(option);
  });
}

// ============= Delete User =============
async function deleteUser() {
  const userId = document.getElementById('deleteUserId').value;
  if (!userId) {
    setText('deleteUserMessage', `<span class="text-danger">❌ Please select a user to delete.</span>`);
    return;
  }

  const res = await fetch(`${API_BASE}/admin/delete_user`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id: userId })
  });

  const data = await res.json();
  if (res.ok) {
    setText('deleteUserMessage', `<span class="text-success">✅ ${data.message}</span>`);
    await loadUsers();
  } else {
    setText('deleteUserMessage', `<span class="text-danger">❌ ${data.error}</span>`);
  }
}

// ============= Fetch Audit Logs =============
async function fetchAuditLogs() {
  const table = document.getElementById('auditLogsTable');
  table.innerHTML = '<tr><td colspan="4" class="text-center">Loading...</td></tr>';

  const res = await fetch(`${API_BASE}/admin/audit_logs`);
  const data = await res.json();

  if (data.logs.length === 0) {
    table.innerHTML = '<tr><td colspan="4" class="text-center">No logs found.</td></tr>';
    return;
  }

  table.innerHTML = '';
  data.logs.forEach(log => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${log.event || ''}</td>
      <td>${log.status || ''}</td>
      <td>${log.user_id || ''}</td>
      <td>${log.timestamp || ''}</td>
    `;
    table.appendChild(row);
  });
}
