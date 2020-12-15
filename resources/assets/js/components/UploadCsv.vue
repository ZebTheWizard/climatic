<template>
  <bootstrap-card savable="" title="Upload from CSV" @save="save">
    <p>Test upload with <a :href="'/example.csv'" download>Example.csv</a></p>
    <vue-csv-import
      v-if="visible"
      ref="csv"
      v-model="parseCsv"
      :autoMatchFields="true"
      :autoMatchIgnoreCase="true"
      :headers="true"
      :map-fields="{
        created_at: 'created_at',
        humidity: 'humidity',
        celsius: 'celsius',
      }"
    >
      <template slot="next">
        <span></span>
        <!-- <button @click.prevent="load">load!</button> -->
      </template>
    </vue-csv-import>
    <!-- <button
      class="btn text-white float-end btn-sm theme-ignore btn-success"
      @click="load"
      v-show="!loaded && hasFile"
    >
      <span class="mx-2">Load</span>
    </button> -->
    <div v-if="loaded">
      <button
        class="btn text-white float-end btn-sm theme-ignore btn-primary"
        @click="save"
      >
        <span class="mx-2">Save</span>
      </button>
      <button
        class="btn text-white float-end btn-sm theme-ignore btn-danger mx-2"
        @click="discard"
      >
        <span class="mx-2">Discard</span>
      </button>
    </div>
  </bootstrap-card>
</template>

<script>
import { VueCsvImport } from "vue-csv-import";
import { EventBus } from "./EventBus.js";

export default {
  components: {
    VueCsvImport,
  },
  data() {
    return {
      parseCsv: null,
      loaded: false,
      visible: true,
      hasFile: false,
    };
  },
  mounted() {
    var input = this.$refs.csv.$refs.csv;
    input.addEventListener("change", (e) => {
      console.log("file changed");
      this.hasFile = input.files.length > 0;
      try {
        this.load();
      } catch (err) {}
    });
  },
  methods: {
    load() {
      console.log("changed csv");
      this.$refs["csv"].load();
      this.loaded = true;
    },
    discard() {
      this.loaded = false;
      this.visible = false;
      this.$nextTick(() => {
        this.visible = true;
      });
      this.parseCsv = {};
    },
    save() {
      axios
        .post("/entry/upload", { rows: this.parseCsv })
        .then((res) => {
          this.discard();
          EventBus.$emit("csv");
        })
        .catch((res) => {
          this.discard();
        });
    },
  },
};
</script>

<style>
</style>