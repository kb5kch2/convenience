'''
폴더를 복사할 때 복사되지 않은 파일이 뭔지 알아보기~
'''
import os
import shutil
import copy

# # 복사한 폴더 경로
# copied_folder_path = 'C:/Users/dohun/Downloads/test/'
# # 붙여넣은 폴더 경로
# pasted_folder_path = 'C:/Users/dohun/Downloads/test2/'

def files_in_folder(folder_path, want_print=False):
    '''
    폴더 안에 있는 "파일.확장자"를 리스트에 넣기
    '''
    files_list = []
    for (root, directories, files) in os.walk(folder_path):
        for file in files:
            file_name = os.path.join(file)
            files_list.append(file_name)
    if want_print:
        print('폴더', folder_path, '안에 있는 파일들')
        if len(files_list) == 0:
            print('    폴더가 비어있습니다.')
        else:
            print(f'    총 {len(files_list)}개')
            for file in files_list:
                print('   ', file)
    return files_list

def find_absence_files(copied_folder, pasted_folder, copied_folder_path, want_print=False):
    '''
    복사한 폴더와 붙여넣은 폴더 동시에 들어있지 않은 파일 찾기
    '''
    uncopied_file_list = []
    for cp_file in copied_folder:
        cnt = 0
        for pst_file in pasted_folder:
            if cp_file != pst_file:
                cnt += 1
        if cnt == len(pasted_folder):
            uncopied_file_list.append(cp_file)
    uncopied_file_list_for_print = copy.copy(uncopied_file_list)
    for i, file in enumerate(uncopied_file_list):
        uncopied_file_list[i] = copied_folder_path + file
    if want_print:
        print('복사되지 않은 파일들')
        if len(uncopied_file_list_for_print) == 0:
            print('    복사되지 않은 파일이 없습니다.')
        else:
            print(f'    총 {len(uncopied_file_list_for_print)}개')
            for file in uncopied_file_list_for_print:
                print('   ', file)
    return uncopied_file_list

def copy_uncopied_files_n_print(uncopied_files_list ,pasted_folder_path):
    for file in uncopied_files_list:
        shutil.copy(file, pasted_folder_path)
    print(f"@@@@@ {len(uncopied_files_list)}개 파일의 복사가 완료되었습니다. @@@@@")

def copy_uncopied_files(copied_folder_path, pasted_folder_path, print_files_list=False):
    '''
    copied_folder_path: 복사한 폴더 경로
    pasted_folder_path: 붙여넣기한 폴더 경로
    print_files_list: 폴더 안의 파일들을 출력하고 싶으면 True로
    '''
    cp_folder = files_in_folder(copied_folder_path, print_files_list)
    ps_folder = files_in_folder(pasted_folder_path, print_files_list)
    files = find_absence_files(cp_folder, ps_folder, copied_folder_path, print_files_list)
    copy_uncopied_files_n_print(files, pasted_folder_path)