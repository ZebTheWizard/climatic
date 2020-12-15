<template>
  <bootstrap-card
    savable="Save"
    title="Input Single Entry"
    @save="save"
    :saving="saving"
    :error="error"
  >
    <div class="row mb-3">
      <div class="col-4 text-start">Datetime</div>
      <div class="col-4 text-center">Humidity</div>
      <div class="col-4 text-end">Celsius</div>
    </div>
    <div class="row">
      <date-picker
        class="col-4"
        v-model="datetime"
        type="datetime"
      ></date-picker>
      <div class="col-4 flex-center flex-wrap">
        <vue-slider
          class="w-100"
          v-model="humidity"
          :interval="0.1"
          :tooltip="true"
        ></vue-slider>
        <label class="small text-muted">use arrow keys</label>
      </div>
      <div class="col-4">
        <div class="input-group">
          <input
            type="number"
            class="form-control"
            placeholder="temp"
            step="0.1"
            v-model="celsius"
          />
          <div class="input-group-append">
            <span class="input-group-text" id="basic-addon2">C</span>
          </div>
        </div>
      </div>
    </div>
  </bootstrap-card>
</template>

<script>
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/antd.css";
export default {
  components: {
    DatePicker,
    VueSlider,
  },
  data() {
    return {
      datetime: new Date(),
      humidity: 30,
      celsius: 14,
      saving: false,
      error: false,
    };
  },

  methods: {
    save() {
      this.saving = true;
      this.error = false;
      axios
        .post("/entry/add", {
          datetime: moment(this.datetime).format("YYYY-MM-DD HH:mm:ss"),
          humidity: this.humidity,
          celsius: this.celsius,
        })
        .then((res) => {
          this.saving = false;
        })
        .catch((err) => {
          this.saving = false;
          this.error = true;
        });
    },
  },
};
</script>

<style>
.vue-slider-rail {
  background-color: var(--bs-gray);
  isolation: isolate;
  z-index: 1000;
}

.vue-slider-process {
  background-color: var(--bs-primary);
}
</style>