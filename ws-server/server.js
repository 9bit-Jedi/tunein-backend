
const WebSocket = require("ws");
const PORT = 8080;

const { WebSocketServer } = require("ws");
// const sockserver = new WebSocketServer({ port: 8080 });

// Create a WebSocket server
const wss = new WebSocket.Server({ host: "0.0.0.0", port: PORT });

const broadcast = (data) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      console.log("time", data.currentTime);
      client.send(JSON.stringify(data));
    }
  });
};

let songState = {
  playing: false,
  currentTime: 0,
};

console.log(`WebSocket server is running on ws://localhost:${PORT}`);

// Handle new connections
wss.on("connection", (ws) => {
  console.log("New client connected");

  // Send current song state to the new client
  broadcast(songState);

  // Handle messages from clients
  ws.on("message", (message) => {
    const data = JSON.parse(message);

    // If it's a play/pause or time update, broadcast it to all clients
    if (
      data.type === "play" ||
      data.type === "pause" ||
      data.type === "time_update"
    ) {
      songState = { ...songState, ...data };
      broadcast(data);
    }
  });

  ws.on("close", () => {
    console.log("Client disconnected");
  });
});
