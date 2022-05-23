<template>
<div class='buzzer_list_wrapper'>
    <b-alert v-model="showMessage" variant="info" show dismissible>{{message}}</b-alert>
    <p>Tigrouroyal: liste des buzzers</p>
    <div class="control">
      <input v-model="addBuzzerForm.id" class="input" type="text" placeholder="Identifiant buzzer">
      <input v-model="addBuzzerForm.nom" class="input" type="text" placeholder="Nom buzzer">
    </div>    
    <button type="button" @click="onAddBuzzer()">Add Buzzer</button>
    <template v-for="(buzzer) in buzzers" :key="buzzer.id">
        <div class="buzzer_list_item">
            <div class="buzzer_list_buzzer">{{buzzer.id}} / {{buzzer.nom}} </div>
            <button type="button" @click="onDeleteBuzzer(buzzer)">Delete Buzzer</button>
            <button type="button" @click="onActivateBuzzer(buzzer)">Activate Buzzer</button>
        </div>
    </template>
</div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'BuzzerList',
  data() {
    return {
      buzzers: [],
      addBuzzerForm : {
        id: '',
        nom: ''
      },
      message: '',
      showMessage: false,
    };
  },
  methods: {
    addBuzzer(payload) {
      const path = 'http://localhost:5000/api/buzzer';
      axios.post(path, payload)
        .then(() => {
          this.getBuzzers();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBuzzers();
        });
    },
    getBuzzers() {
      const path = 'http://localhost:5000/api/buzzer';
      axios.get(path)
        .then((res) => {
          this.buzzers = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    initForm() {
      this.addBuzzerForm.id = '';
      this.addBuzzerForm.nom = '';
    },
    onAddBuzzer() {
      if (this.addBuzzerForm.id == '') {
        this.message = 'Buzzer Identifiant is required!';
        this.showMessage = true;        
      } else if (this.addBuzzerForm.nom == '') {
        this.message = 'Buzzer Nom is required!';
        this.showMessage = true;        
      } else {   
        const payload = {
          id: this.addBuzzerForm.id,
          nom: this.addBuzzerForm.nom,
        };
        this.addBuzzer(payload);
        this.initForm();
      }
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBuzzerModal.hide();
      this.initForm();
    },
    removeBuzzer(buzzerID) {
      const path = `http://localhost:5000/api/buzzer/${buzzerID}`;
      axios.delete(path)
        .then(() => {
          this.getBuzzers();
          this.message = 'Buzzer removed!';
          this.showMessage = true;
      })
        .catch((error) => {
        // eslint-disable-next-line
          console.error(error);
          this.getBuzzers();
      });
    },
    onDeleteBuzzer(buzzer) {
      this.removeBuzzer(buzzer.id);
    },
    activateBuzzer(buzzerID) {
      const path = `http://localhost:5000/api/buzzer/activate/${buzzerID}`;
      axios.get(path)
        .then(() => {
          this.getBuzzers();
          this.message = 'Buzzer activated!';
          this.showMessage = true;
      })
        .catch((error) => {
        // eslint-disable-next-line
          console.error(error);
          this.getBuzzers();
      });
    },
    onActivateBuzzer(buzzer) {
      this.activateBuzzer(buzzer.id);
    },
  },
  created() {
    this.getBuzzers();
  },
};
</script>

