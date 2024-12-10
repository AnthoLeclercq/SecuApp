import { RootState } from "app/rootReducer";
import { CurrentUser } from "features/User/UserType";
import { useSelector } from "react-redux";
import { authLogin, resetAuthState } from "./authSlice";
import { fetchApi } from "features/rest";
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


export const useCurrentUser = () => {
    const { user } = useSelector((state: RootState) => state.auth);
    return user;
}

export const useLogged = () => {
    const { logged } = useSelector((state: RootState) => state.auth);
    return logged;
}

export const logout = () => async (dispatch) => {
    dispatch(resetAuthState())
}

export const loginUser = (data: FormData, funcSuccess: () => void) => async (dispatch: any) => {
    try {
      const formData = new FormData();
      formData.append('email', data.get('email')!);
      formData.append('password', data.get('password')!);
  
      fetchApi({
        method: 'POST',
        endpoint: '/authenticate',
        data: formData,
        funcSuccess: (responseData) => {
          dispatch(getUser(responseData.token, funcSuccess));
        },
        dispatch
      });
    }  catch (err) {
        toast.error('Une erreur s\'est produite. Veuillez réessayer.');
      }
  };

  export const getUser = (token: string, funcSuccess: () => void) => async (dispatch: any) => {
    fetchApi({
      method: 'GET',
      endpoint: '/me',
      token: token,
      funcSuccess: (data) => {
        dispatch(() => {
          const currentUser: CurrentUser = data.user;
          currentUser.token = token;
          dispatch(authLogin(currentUser));
        });
        funcSuccess();
      },
      dispatch
    });
  };
  
  export const registerUser = (token: string,data: FormData, funcSuccess: () => void) => async (dispatch: any) => {
    try {
 
      fetchApi({
        method: 'POST',
        endpoint: '/register',
        token: token,
        data: data,
        funcSuccess: () => {
          funcSuccess();
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

