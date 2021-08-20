<template>
<div class="modal" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">New Entry</h5>
        <button type="button" v-on:click="$emit('showentryform')" class="close" data-dismiss="modal" aria-label="Close" :ref="'newEntry'">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">

        <form>

          <div class="form-group">
            <label>Entry Date</label>
            <date-picker v-model="pickedDate" :input-class="'form-control form-control-sm'"></date-picker>
          </div>

          <div class="form-group">
            <label for="category">Category</label>
            <select v-model="entryForm.category" v-on:change="onCategorySelection" id="category" class="form-control form-control-sm">
              <option disabled>Pick a category</option>
                <optgroup v-for="category of categories" :label="category.title">
                  <option v-for="child of category.children" :ref="'category_' + child.id" v-bind:value="child.id">{{ child.title }}</option>
                </optgroup>
            </select>
          </div>

          <div class="form-group">
            <label for="account">Account</label>
            <select v-model="entryForm.account" v-on:change="onAccountSelection" id="account" class="form-control form-control-sm">
              <option disabled>Pick an account</option>
                <optgroup v-for="account of accounts" :label="account.title">
                  <option v-for="child of account.children" :ref="'account_' + child.id" v-bind:value="child.id">{{ child.title }}</option>
                </optgroup>
            </select>
          </div>

          <div class="form-group">
            <label for="item">Item</label>
            <vue-simple-suggest
              v-model="entryForm.item"
              :list="records"
              :display-attribute="'item'"
              :value-attribute="'id'"
              :filter-by-query="true"
              :styles="autoCompleteStyle"
              v-on:suggestion-click="onSuggestClick"
              @select="onSuggestClick"
              :value="entryForm.item"
              :placeholder="'New Item'"
              :id="'item'"
              autocomplete="off">
              <!-- Filter by input text to only show the matching results -->
            </vue-simple-suggest>
          </div>

          <div class="form-group">
            <label for="value">Value</label>
            <input v-model.number="entryForm.value" type="number" class="form-control form-control-sm" id="value" placeholder="0.00">
          </div>
        </form>

      </div>
      <div class="modal-footer">
        <button type="submit" v-on:click="submitForm" class="btn btn-primary">Submit</button>
        <button type="button" v-on:click="$emit('showentryform')" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>

import axios from 'axios';
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import VueSimpleSuggest from 'vue-simple-suggest'
import 'vue-simple-suggest/dist/styles.css' // Optional CSS

export default {
  components: {
    'date-picker': DatePicker,
    'vue-simple-suggest': VueSimpleSuggest,
  },
  props: [],
  data () {
    return {
      categories: "",
      accounts: "",
      records: [],
      records2: [],
      child: "",
      selectedAccount: "",
      pickedDate: new Date,
      entryForm: {
        date: 0,
        category: "Pick a category",
        account: "Pick an account",
        item: "",
        value: "",
      },
      autoCompleteStyle : {
        vueSimpleSuggest: "position-relative",
        inputWrapper: "",
        defaultInput : "form-control form-control-sm",
        suggestions: "position-absolute list-group z-1000",
        suggestItem: "list-group-item"
      },
      handpickedCategory: false,
      handpickedAccount: false,
    }
  },

  mounted() {
    this.pickTodaysDate();
    this.loadCategories();
    this.loadAccounts();
    this.loadRecords();
    this.$refs.newEntry.focus();
  },

  methods: {

    onCategorySelection() {
      this.handpickedCategory = true;
      
    },

    onAccountSelection() {
      this.handpickedAccount = true;
      
    },

    submitForm () {
      this.entryForm.date = this.pickedDate.toLocaleDateString("se-SE");
      console.log('Form submitted');
      console.log(this.entryForm);
      axios
        .post('/records/', this.entryForm)
        .then((response) => {
          console.log(response)
          this.$notify({
              group: 'alertSuccess',
              title: 'New entry addedd',
              text: 'New entry have been addedd!',
            });
          this.entryForm.date = new Date;
        })
        .catch((error) => {
          this.$notify({
              group: 'alertFail',
              title: 'Error',
              text: 'There has been an error',
            });
        });
    },

    pickTodaysDate() {
      var date = new Date();
      this.entryForm.date = date;
    },

    loadCategories() {
      axios
        .get('/categories/')
        .then((response) => { 
          this.categories = this.$nestObjects(response.data);
        });
    },

    loadAccounts() {
      axios
        .get('/accounts/')
        .then((response) => { 
          this.accounts = this.$nestObjects(response.data);
        });
    },

    loadRecords() {
      axios
        .get('/records-suggest/')
        .then((response) => { 
          this.records = response.data;
        });
    },

    onSuggestClick(suggestionObject) {
      if (!this.handpickedAccount) {
        this.entryForm.account = suggestionObject['account'];
      }
      if (!this.handpickedCategory) {
        this.entryForm.category = suggestionObject['category'];
      }
    },


  },

  computed: {

  },
}
</script>

<style>

.mx-datepicker {
  display: block;
}
</style>
