<template>
  <div class="container-fluid">
    <div class="row">

      <div class="col-xl-4 col-lg-5">
        <accounts-balance/>
      </div>

      <div class="col-xl-4 col-lg-5">
        <div class="card">
          <div class="card-header">
            <div class="col text-center">
              <date-picker v-on:input="loadCategories" v-model="defaultRange" range></date-picker>
            </div>
          </div>
          <div class="card-body">
            <dashboard-chart :chart-data="datacollection"></dashboard-chart>
          </div>
        </div>
      </div>

      <div class="col-xl-4 col-lg-5"> <!--column-->
        <last-entries/>
      </div>

    </div>
  </div>
</template>

<script>

import DashboardChart from '../components/DashboardChart.vue'
import LastEntries from '../components/LastEntries.vue'
import AccountsBalance from '../components/AccountsBalance.vue'
import axios from 'axios';
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';

export default {
  components: {
    'date-picker': DatePicker,
    'dashboard-chart': DashboardChart,
    'last-entries': LastEntries,
    'accounts-balance': AccountsBalance,
  },
  props: [],
  data () {
    return {
      defaultRange: this.getDateRangeCurrMonth(),
      categories: this.loadCategories(),
      category: 0,
      child: 0,
      vue: 1,
      datacollection: new Object(),
      options: { 
        responsive: true,
        maintainAspectRatio: false
      },
    }
  },

  mounted() {
    console.log('dashboard mounted');
  },

  methods: {
    fillChart() {
      this.datacollection = {}
      var labels = [];
      var data = [];
      var backgroundColor = ['LightBlue', 'Green', 'Beige', 'LightPink', 'LightBlue', 'DarkBlue', 'DarkGreen']
      var datasets = [];

      for (var category of this.categories) {
        for (var child of category.children) {
          labels.push(child.title);
          data.push(child.expenses);
        }
      }

      var dataset = {
        'data': data,
        'labels': labels,
        'backgroundColor': backgroundColor
      };
      datasets.push(dataset);
      this.datacollection['labels'] = labels;
      this.datacollection['datasets'] = datasets;
    },

    loadCategories() {
      axios
        .get('/categories/expenses/')
        .then((response) => { 
          for (var cat of response.data) {
            cat['expenses'] = 0;
          }
          this.getExpensesSummary(this.defaultRange, response.data);
        });
    },

    calculateParent() {
      for (var category of this.categories) {
        var categorySum = 0;
        for (var child of category.children) {
          categorySum += child.expenses;
        }
        category.expenses = categorySum;
      }
    },

    log(message) {
      console.log(message);
    },

    getDateRangeCurrMonth() {
      var date = new Date();
      date.setTime( date.getTime() + date.getTimezoneOffset()*60*1000 );
      var firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
      // for testing
      var firstDay = new Date(date.getFullYear(), 0, 1);
      var lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
      return [firstDay, lastDay];
    },

    formatDate(dateRange) {
      var rangeStart = dateRange[0];
      var rangeEnd = dateRange[1];
      var result = [];

      for (var range of dateRange) {
        range = range.getFullYear() + '-' + ('0' + (range.getMonth()+1)).slice(-2) + '-' + ('0' + range.getDate()).slice(-2);
        result.push(range);
      }

      return result[0]+'-'+result[1];
    },
    
    getExpensesSummary(dateRange, categoryData) {
      let promises = [];

      for (var category of categoryData) {
        promises.push(axios.get('/categories/'+category.id+'/sum/'+this.formatDate(dateRange)));
      }

      axios.all(promises).then((response) => {
      
        for (var idx = 0; idx < categoryData.length; idx++) {
          var val = response[idx].data.value__sum;
          if (val == null) {
            val = 0;
          }
          categoryData[idx]['expenses'] = val;
        }

        this.categories = this.$nestObjects(categoryData);
        this.calculateParent();
        this.fillChart();
      });
      
    },

  },

  computed: {

  },
}
</script>

<style>
</style>
