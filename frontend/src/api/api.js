import axios from "axios";
import { useAppStore } from "@/stores/store";

let BASE_URL = "/api/v1";

if (import.meta.env.MODE === "development") {
  BASE_URL = "https://elitawork.com/api/v1";
}

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const getJobs = async () => {
  try {
    const res = await api.get("positions");

    if (res.status !== 200) {
      return {
        success: false,
        data: res.data,
      };
    }

    useAppStore().setJobs(res.data);

    return {
      success: true,
      data: res.data,
    };
  } catch (error) {
    return {
      success: false,
      data: error.response.data,
    };
  }
};

export const getEmployees = async () => {
  try {
    const res = await api.get(`managers`);

    if (res.status !== 200) {
      return {
        success: false,
        data: res.data,
      };
    }
    useAppStore().setEmployees(res.data);
    return {
      success: true,
      data: res.data,
    };
  } catch (error) {
    return {
      success: false,
      data: error.response.data,
    };
  }
};

export const getPartners = async () => {
  try {
    const res = await api.get(`partners`);

    if (res.status !== 200) {
      return {
        success: false,
        data: res.data,
      };
    }

    return {
      success: true,
      data: res.data,
    };
  } catch (error) {
    return {
      success: false,
      data: error.response.data,
    };
  }
};
