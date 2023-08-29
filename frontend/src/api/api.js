import axios from "axios";
import { useAppStore } from "@/stores/store";

const BASE_URL = "http://elitawork.yuriipalamarchuk.com/api/v1";

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

    console.log(res.data);

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
