const course_selector = document.getElementById("course-selector");
const lesson_selector = document.getElementById("lesson-selector");
const lesson_name_inp = document.getElementById("lesson-name");
const video_link_inp = document.getElementById("video-link");
const api_server = "http://130.193.58.142:8000";

let courses = [];

fetch(api_server + "/get-courses").then(r =>
    r.json().then(fetched_courses => {
        courses = fetched_courses;
        course_selector.innerHTML = "";
        courses.forEach(course => {
                let opt = document.createElement("option");
                opt.value = course.id;
                opt.innerText = course.title;
                course_selector.appendChild(opt);
            }
        )
    })
)