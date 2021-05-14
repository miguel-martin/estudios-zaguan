<script language="javascript" type="text/javascript">

    const buildOptionFromEntry = (cod, val) => {
        return `<option value="${cod}">${val}</option>`
    };

    const buildSelectFromJson = (data) => {
        console.log('Construyendo select de PD...')
        out = '<select id="programasdoct">'
        for (let pd in data) {
            out += buildOptionFromEntry(pd, data[pd])
        }
        out += '</select>'
        return out
    };

    const getProgramasDoctorado = () => {
        console.log('Obteniendo programas de doctorado...');
        fetch('/uz_scripts/programas-doctorado', {
            method: 'get'
        })
       //.then(response => response.text())
       .then(response => response.json())
       .then(data => {
              document.querySelector('#pd-wrapper').innerHTML=buildSelectFromJson(data)
        })
       .catch(err => {
           console.log('Error obteniendo programas de doctorado', err)
        })
    };

    document.addEventListener('DOMContentLoaded', () => {
        // Cuando este cargado el DOM, obtener los PD
        getProgramasDoctorado();
    });

</script>

<div id="pd-wrapper">Cargando programas de doctorado...</div>
