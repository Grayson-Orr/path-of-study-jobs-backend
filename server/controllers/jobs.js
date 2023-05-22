import csv from "csv-parser";
import fs from "fs";

const getJobs = async (req, res) => {
  try {
    const filePath = "../web-scraper/job/data.csv";
    const jobs = await parseCSVFile(filePath);
    res.status(200).json(jobs);
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
