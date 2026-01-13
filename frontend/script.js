const API = "http://localhost:8000/api";

async function upload() {
  const file = document.getElementById("fileInput").files[0];
  if (!file) return alert("Select a file");

  const data = new FormData();
  data.append("file", file);

  await fetch(`${API}/documents`, { method: "POST", body: data });
  alert("Document indexed");
}

async function ask() {
  const query = document.getElementById("question").value;

  const res = await fetch(`${API}/qa`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.answer;
}
