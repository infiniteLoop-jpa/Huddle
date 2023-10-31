// Django project name: Huddle
// Django app name: Huddle_app
// Course: CS 4800 - SWE

document.addEventListener('DOMContentLoaded', () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    if (event.code === 'Escape') {
      closeAllModals();
    }
  });
});



function createHuddle() {
  // obtain values from user input from id="createHuddleForm"
  var huddleName = document.getElementById('huddleName').value;
  var description = document.getElementById('description').value;

  // Huddle group card html template
  var huddleTemplate = `
  <div class="column is-one-third">
            <div class="card">
              <div class="card-image">
                <figure class="image">
                  <img src="/static/huddle_default.png" alt="default huddle photo">
                </figure>
              </div>
              <div class="card-content card-content-size">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">${huddleName}</p>
                    <p class="subtitle is-6">${description}</p>
                  </div>
                </div>
              </div>
            </div>
      </div>
  `;
  // Insert HTML to id="cardContainer"
  const cardContainer = document.getElementById('cardContainer');
  cardContainer.insertAdjacentHTML('beforeend', huddleTemplate);
}
