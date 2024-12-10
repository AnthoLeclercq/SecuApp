import { fetchApi } from "features/rest";
import { CurrentUser, User } from "./UserType";
import { logout } from "features/Auth/authApi";
import { Navigate } from "react-router-dom";

export const getUsers = (funcSuccess: (data: User[]) => void, token: string) => async (dispatch: any) => {
  fetchApi({
    method: 'GET',
    endpoint: '/user',
    token: token,
    funcSuccess: (data) => {
      funcSuccess(data);
    },
    dispatch
  });
};


export const deleteUser = (idUser: number, token: string, currentUser: CurrentUser|null,funcSuccess: () => void) => async (dispatch) => {
  fetchApi({
    method: 'DELETE',
    endpoint: `/user/${idUser}`,
    token: token,
    funcSuccess: (responseData) => {
      if( currentUser && idUser === currentUser.id){
        dispatch(logout());
      }else{
        funcSuccess();
      }   
    },
    dispatch
  });
}

export const updateUser = (data: Object, idUser: number, token: string, funcSuccess: (data: CurrentUser) => void) => async (dispatch: any) => {
  fetchApi({
    method: 'PUT',
    endpoint: `/user/${idUser}`,
    token: token,
    data: data,
    funcSuccess: (responseData) => {
      funcSuccess(responseData);
    },
    dispatch
  });
};
