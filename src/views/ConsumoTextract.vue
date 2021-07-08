<template>
  <div class="profile-page">
    <section class="section-profile-cover section-shaped my-0">
      <div class="shape shape-style-1 shape-primary shape-skew alpha-4"></div>
    </section>
    <section class="section section-skew">
      <div class="container">
        <card shadow class="card-profile mt--300" no-body>
          <div class="px-4">
            <div class="row justify-content-center"></div>
            <div class="text-center mt-5">Consumo TEXTRACT</div>
            <div class="mt-5 py-5 border-top text-center">
                    <label
                      >File
                      <input
                        type="file"
                        id="file"
                        ref="file"
                        v-on:change="handleFileUpload()"
                      />
                    </label>
                    <button v-on:click="submitFile()">Submit</button>
              <input type="text"> <button>buscar resultado</button>
            </div>
            
          </div></card
        >
      </div>
    </section>
  </div>
</template>
            </div>
          </div>
        </card>
      </div>
    </section>
  </div>
</template>
<script>
  export default {
    /*
      Defines the data used by the component
    */
    data(){
      return {
        file: ''
      }
    },

    methods: {
      /*
        Submits the file to the server
      */
      submitFile(){
        var axios = require("axios");
        let formData = new FormData();

        formData.append('arquivo_pdf', this.file);

        axios.post('http://127.0.0.1:3000/processamento',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
        ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },

      /*
        Handles a change on the file upload
      */
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>
<style>
</style>
