async function loadState() {
  try {
    const res = await fetch("/api/state");
    if (!res.ok) throw new Error("Failed to fetch state");
    return await res.json();
  } catch (err) {
    console.error(err);
    // fallback demo data
    return {
      pot: 0,
      community: ["—", "—", "—", "—", "—"],
      players: [],
      hand: []
    };
  }
}

function renderCard(value) {
  const el = document.createElement("div");
  el.className = value === "—" ? "card empty" : "card";
  el.textContent = value;
  return el;
}

function render(players, community, pot, hand) {
  document.getElementById("pot").textContent = `$${pot}`;
  const communityEl = document.getElementById("community");
  communityEl.innerHTML = "";
  community.forEach(c => communityEl.appendChild(renderCard(c)));

  const handEl = document.getElementById("hand");
  handEl.innerHTML = "";
  hand.forEach(c => handEl.appendChild(renderCard(c)));

  const playersEl = document.getElementById("players");
  playersEl.innerHTML = "";
  players.forEach(p => {
    const card = document.createElement("div");
    card.className = `player${p.is_self ? " self" : ""}`;
    card.innerHTML = `
      <div class="name">${p.name}</div>
      <div class="stack">Stack: $${p.stack} • Bet: $${p.bet}</div>
      <div class="status">${p.status || ""}</div>
    `;
    playersEl.appendChild(card);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  const state = await loadState();
  render(state.players, state.community, state.pot, state.hand);
});
