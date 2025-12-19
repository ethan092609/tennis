import readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Fake database
const mockPlayers = {
  "TenZ#NA1": {
    headshot: "24.6%",
    kd: "1.32",
    winRate: "54.1%",
    acs: "251"
  },
  "Asuna#100T": {
    headshot: "22.3%",
    kd: "1.18",
    winRate: "51.7%",
    acs: "238"
  }
};

rl.question("Enter Valorant player tag (Username#Tag): ", (playerTag) => {
  if (!playerTag.includes("#")) {
    console.log("❌ Invalid format. Use Username#Tag");
    rl.close();
    return;
  }

  const stats = mockPlayers[playerTag];

  if (!stats) {
    console.log("❌ Invalid player.");
    rl.close();
    return;
  }

  console.log("\n🎯 VALORANT STATS");
  console.log("----------------------------");
  console.log(`Headshot %: ${stats.headshot}`);
  console.log(`K/D Ratio: ${stats.kd}`);
  console.log(`Win Rate: ${stats.winRate}`);
  console.log(`Average Combat Score: ${stats.acs}`);
  console.log("----------------------------");

  rl.close();
});
