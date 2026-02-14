export async function generateIntel(profile) {
  const res = await fetch("http://localhost:8000/generate", {
    method:"POST",
    headers:{ "Content-Type":"application/json" },
    body:JSON.stringify({ profile })
  });

  return await res.json();
}
