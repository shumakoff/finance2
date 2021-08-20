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
  data () {
    return {
      options: { 
        legend : {
          display: false
        }
      }
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
