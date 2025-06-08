    document.addEventListener("DOMContentLoaded", function () {
        const isOrgCheckbox = document.getElementById('id_is_organisation');
        const orgDiv = document.getElementById('org-div');
        const addressChoice = document.getElementById('address_choice');
        const existingAddress = document.getElementById('existing-address');
        const newAddress = document.getElementById('new-address');

            const isIndividual = document.getElementById("id_is_individual");
    const isOrganisation = document.getElementById("id_is_organisation");

    isIndividual.addEventListener("change", function () {
        if (this.checked) {
            isOrganisation.checked = false;
        }
    });

    isOrganisation.addEventListener("change", function () {
        if (this.checked) {
            isIndividual.checked = false;
        }
    });

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
