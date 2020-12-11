<template>
  <div :class="['theme-overlay', currentTheme]"></div>
</template>

<script>
import { EventBus } from "./EventBus";
export default {
  props: {
    theme: {
      type: String,
      default: "default",
    },
  },
  data() {
    return {
      currentTheme: "default",
    };
  },
  mounted() {
    this.currentTheme = this.theme;
    document.body.classList.add("has-theme");
    document.body.classList.add(this.currentTheme);

    if (this.currentTheme !== "default") {
      this.$nextTick(() => {
        EventBus.$emit("theme-default", this.currentTheme == "dark");
        console.log("should emit default theme");
      });
    }

    console.log(this.currentTheme);
    EventBus.$on("theme", (isDark) => {
      console.log("getting theme", isDark);
      this.setTheme(isDark ? "dark" : "light");
    });
  },
  methods: {
    setTheme(theme) {
      this.currentTheme = theme;
      document.body.classList.remove("light");
      document.body.classList.remove("dark");
      document.body.classList.remove("default");
      document.body.classList.add(this.currentTheme);
    },
  },
};
</script>

<style>
</style>