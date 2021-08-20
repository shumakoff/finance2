<script>

import { Doughnut, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins;

export default {
  extends: Doughnut,
  mixins: [reactiveProp],
  props: {
    chartdata: {
      type: Object,
      default: null
    }
  },
  options: {
  },

  mounted() {
    this.renderChart(this.chartData, this.options);
  },

  components: {
  },

  methods: {
  },

  computed: {
  },
}
</script>

<style>
</style>
