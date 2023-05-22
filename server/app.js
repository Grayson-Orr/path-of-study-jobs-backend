import compression from "compression";
import dotenv from "dotenv";
import express, { urlencoded, json } from "express";

import jobs from "./routes/jobs.js";

dotenv.config();

const app = express();

const BASE_URL = "api";
const CURRENT_VERSION = "v1";
const PORT = process.env.PORT;

app.use(urlencoded({ extended: false }));
app.use(json());
app.use(compression());

app.use(`/${BASE_URL}/${CURRENT_VERSION}/jobs`, jobs);

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
