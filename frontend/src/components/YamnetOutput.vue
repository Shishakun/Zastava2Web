<template>
  <div>
    <button @click="toggleYamnet">
      {{ startYamnet ? "Stop Yamnet" : "Start Yamnet" }}
    </button>
    <div
      :class="{
        'bg-[#232323]': true,
        'bg-red-500': isRedBackground(),
      }"
      class="font-roboto text-xl font-bold border-[#535353] text-white border-[1.5px] px-4 py-2 rounded-xl"
    >
      {{ yamnetResult }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      yamnetResult: null,
      startYamnet: false,
      classesWithRedBackground: [
        "Gunshot",
        "gunfire",
        "Machine gun",
        "Explosion",
        "Artillery fire",
        "Cap gun",
        "Boom",
        "Fireworks",
        "Firecracker",
        "Police car (siren)",
        "Ambulance (siren)",
        "fire truck (siren)",
        "Engine",
        "Siren",
        "Alarm",
        "Jet engine",
        "Foghorn",
        "Aircraft",
        "Helicopter",
      ],
    };
  },
  mounted() {
    this.fetchYamnetResult();
    this.interval = setInterval(this.fetchYamnetResult, 2000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },
  methods: {
    async fetchYamnetResult() {
      if (this.startYamnet) {
        try {
          const response = await fetch("http://localhost:8000/yamnet");
          const data = await response.json();

          if (data.result && data.result.length > 0) {
            const result = data.result[0];
            const formattedResult = this.formatResult(result);
            this.yamnetResult = formattedResult;
          } else {
            this.yamnetResult = "No result available";
          }

          console.log(data);
          console.log(this.yamnetResult);
        } catch (error) {
          console.error(error);
        }
      }
    },
    toggleYamnet() {
      this.startYamnet = !this.startYamnet;
    },
    isRedBackground() {
      if (this.yamnetResult) {
        for (const className of this.classesWithRedBackground) {
          if (this.yamnetResult.includes(className)) {
            return true;
          }
        }
      }
      return false;
    },
    formatResult(result) {
      const parts = result.split(";").map((part) => part.trim());
      const formattedParts = parts.map((part) => {
        const [label, value] = part.split(":").map((el) => el.trim());
        return `${label}: ${value}`;
      });
      return `Текущее событие: ${formattedParts.join("; ")}`;
    },
  },
};
</script>
