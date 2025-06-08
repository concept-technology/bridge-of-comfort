 
 document.addEventListener("DOMContentLoaded", function () {
        const isOrgCheckbox = document.getElementById('id_is_organisation');
        const orgDiv = document.getElementById('org-div');
        const addressChoice = document.getElementById('address_choice');
        const existingAddress = document.getElementById('existing-address');
        const newAddress = document.getElementById('new-address');

        function toggleOrgField() {
            orgDiv.style.display = isOrgCheckbox.checked ? 'block' : 'none';
        }

        function toggleAddressFields() {
            if (addressChoice.value === 'new') {
                newAddress.style.display = 'block';
                existingAddress.style.display = 'none';
            } else {
                newAddress.style.display = 'none';
                existingAddress.style.display = 'block';
            }
        }

        isOrgCheckbox.addEventListener('change', toggleOrgField);
        addressChoice.addEventListener('change', toggleAddressFields);

        toggleOrgField();
        toggleAddressFields();
    });
