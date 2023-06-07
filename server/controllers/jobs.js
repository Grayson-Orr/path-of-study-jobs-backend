import csv from "csv-parser";
import fs from "fs";

const getJobs = async (req, res) => {
  try {
    const filePath = "../web-scraper/job/data.csv";
    const jobs = await parseCSVFile(filePath);

    const technologies = ["react", "azure", "node", "css", "html"];

    const filteredJobs = jobs.filter((job) => {
      let jobMatched = false;
      for (let i = 0; i < technologies.length; i++) {
        const tech = technologies[i];
        const regex = new RegExp(tech, "gi");
        if (job.description.match(regex)) {
          jobMatched = true;
        }
      }
      return jobMatched;
    });

    res.status(200).json(filteredJobs);
  } catch (err) {
    console.log(err);
  }
};

const parseCSVFile = (filePath) => {
  return new Promise((resolve, reject) => {
    const jobs = [];
    fs.createReadStream(filePath)
      .pipe(csv())
      .on("data", (row) => jobs.push(row))
      .on("end", () => resolve(jobs))
      .on("error", (err) => reject(err));
  });
};

export { getJobs };
