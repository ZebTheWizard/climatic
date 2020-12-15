<template>
  <div>
    <button class="btn btn-link theme-ignore" @click="toggleManual">
      Toggle manual entry
    </button>
    <div v-if="manual">
      <single-entry></single-entry>
      <upload-csv></upload-csv>
      
      <bootstrap-card title="Entries">
        <div class="row mb-3">
          <div class="col-3"><strong>Created At<strong></div>
          <div class="col-3"><strong class="float-end">Humidity<strong></div>
          <div class="col-3"><strong class="float-end">Celsius<strong></div>
          <div class="col-3"><strong class="float-end">Edit<strong></div>
        </div>
        <div style="overflow-y: auto; max-height: 70vh; overflow-x: hidden;">
          <div v-for="(entry, index) in entries" :key="index" class="row mb-3">
            <div class="col-3">{{ prettyDate(entry.created_at) }}</div>
            <div class="col-3"><span class="float-end">{{ entry.humidity }}%</span></div>
            <div class="col-3"><span class="float-end">{{ entry.celsius }}C</span></div>
            <div class="col-3">
              <button class="btn btn-danger px-2 theme-ignore float-end btn-sm" @click="remove(entry, index)">
                Delete
              </button>
            </div>
          </div>
          <div v-if="!entries.length">No entries</div>
        </div>
      </bootstrap-card>
    </div>
    <temp-chart></temp-chart>
  </div>
</template>

<script>
import SingleEntry from "./SingleEntry";
import UploadCsv from "./UploadCsv";
import { EventBus } from "./EventBus";
import TempChart from "./TempChart";
export default {
  components: {
    SingleEntry,
    UploadCsv,
    TempChart,
  },
  data() {
    return {
      manual: false,
      entries: [],
    };
  },
  mounted() {
    EventBus.$on("csv", () => {
      this.getEntries();
    });
  },
  methods: {
    prettyDate(date) {
      return moment(date).format("MMM DD, YYYY hh:mm:ss a");
    },
    getEntries() {
      axios.get("/entry/list").then((res) => {
        this.entries = res.data;
      });
    },
    toggleManual() {
      this.manual = !this.manual;
      this.getEntries();
    },
    remove(entry, index) {
      axios
        .post("/entry/remove", { created_at: entry.created_at })
        .then((res) => {
          this.$delete(this.entries, index);
        });
    },
  },
};
</script>

