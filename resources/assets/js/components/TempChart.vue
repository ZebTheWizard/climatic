<template>
  <div class="card mt-4">
    <div class="card-header">
      <!-- <div class="card-title"> -->
      <span class="h3">Weather</span>

      <div class="flex-center my-3">
        <select
          class="form-select"
          style="margin-right: 1rem"
          v-model="currentChart"
          @change="changeChart(currentChart)"
        >
          <option
            v-for="(chart, index) in availableCharts"
            :key="index"
            :selected="currentChart.type == chart.type"
            :value="chart"
          >
            {{ chart.label }}
          </option>
        </select>

        <button
          class="btn btn-outline-primary pull-right mr-3"
          @click="createChart"
        >
          Refresh
        </button>
      </div>

      <!-- </div> -->
    </div>
    <div class="card-body bg-white">
      <canvas ref="canvas" width="400" height="100"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from "chart.js";
import { EventBus } from "./EventBus";

var timeFormat = "MMM DD";

function newDate(days) {
  return moment().add(days, "d").toDate();
}

function newDateString(days) {
  return moment().add(days, "d").format(timeFormat);
}

window.chartColors = {
  red: "rgb(255, 99, 132)",
  orange: "rgb(255, 159, 64)",
  yellow: "rgb(255, 205, 86)",
  green: "rgb(75, 192, 192)",
  blue: "rgb(54, 162, 235)",
  purple: "rgb(153, 102, 255)",
  grey: "rgb(201, 203, 207)",
};

function randomScalingFactor() {
  return (Math.random() > 0.5 ? 1.0 : -1.0) * Math.random() * 100;
}

function futureDates(days) {
  var list = [];
  for (var i = 0; i < days; i++) {
    list.push(newDateString(i));
  }
  return list;
}

var color = Chart.helpers.color;

function dynamicColors(array) {
  return array.map((x) => {
    if (x > 0) {
      return color(window.chartColors.green).alpha(0.5).rgbString();
    } else {
      return color(window.chartColors.red).alpha(0.5).rgbString();
    }
  });
}

function chart(type, label, format) {
  return { type, label, format };
}

export default {
  props: ["uuid", "pool"],
  data() {
    var lastChartRaw = window.localStorage.getItem("chart");
    var lastChart = lastChartRaw ? JSON.parse(lastChartRaw) : null;
    var defaultChart = chart("default", "Last Hour", "h:mm a");
    return {
      chart: null,
      defaultChart,
      currentChart: lastChart || defaultChart,
      currentChartSelection: "",
      availableCharts: [
        defaultChart,
        chart("default", "Last 6 Hours", "h:mm a"),
        chart("last24hours", "Last 24 Hours", "h a"),
        chart("last7days", "Last 7 days", "MMM DD"),
        chart("last30days", "Last 30 days", "MMM DD"),
        chart("last180days", "Last 180 days", "MMM DD"),
        chart("last365days", "Last 365 days", "MMM"),
        chart("all", "All time", "YYYY"),
      ],
    };
  },
  methods: {
    changeChart(chart) {
      this.chart.destroy();
      window.localStorage.setItem("chart", JSON.stringify(chart));
      this.createChart();
    },
    createChart() {
      axios
        .get(`/entry/list/${this.currentChart.type}`)
        .then((res) => {
          console.log(res.data);
          var canvas = this.$refs["canvas"];
          this.chart = new Chart(canvas, {
            type: "line",
            data: {
              labels: res.data.times.map((x) => {
                // var utc = moment.utc(x).toDate();
                return moment(x).format(this.currentChart.format);
              }),
              datasets: [
                {
                  fill: true,
                  label: "Temperature",
                  borderColor: "rgb(0,0,0)",
                  data: res.data.temps,
                },
                {
                  fill: true,
                  label: "Humidity",
                  borderColor: "rgb(255,0,0)",
                  data: res.data.humid,
                },
              ],
            },
            options: {
              animation: {
                duration: 0,
              },
              plugins: {
                filler: {
                  propagate: false,
                },
              },
              scales: {
                xAxes: [
                  {
                    display: true,
                    ticks: {
                      callback: function (dataLabel, index) {
                        return index % 2 === 0 ? dataLabel : "";
                      },
                    },
                  },
                ],
                yAxes: [
                  {
                    ticks: {
                      autoskip: true,
                      maxTicksLimit: 5,
                    },
                  },
                ],
              },
            },
          });
        })
        .catch((res) => {
          console.error(res);
        });
    },
  },
  mounted() {
    this.currentChartSelection = this.currentChart.type;
    this.createChart();
    EventBus.$on("csv", () => {
      this.createChart();
    });
  },
};
</script>

