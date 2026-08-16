import streamlit as st
import ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

st.markdown('<h1 style="text-align: center; font-weight: 800; letter-spacing: -1px;">🎓 EDUMIND AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #B3A3A3; letter-spacing: 1px; margin-bottom: 40px;">THE PRIVATELY HOUSED TEXTBOOK COMPANION • OLD MONEY EDITION</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📁 DOCUMENT HUB")
    uploaded_file = st.file_uploader("Drop your university PDF here", type="pdf", label_visibility="collapsed")
    
    if uploaded_file:
        st.success("📄 Document Securely Anchored!")
        with open("temp_book.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

with col2:
    st.subheader("💬 INTERACTIVE CHAT ROOM")
    
    if uploaded_file:
        with st.spinner("Analyzing text architecture..."):
            loader = PyPDFLoader("temp_book.pdf")
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
            splits = text_splitter.split_documents(docs)
            
            @st.cache_resource
            def load_embeddings():
                return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            
            embeddings = load_embeddings()
            vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
            retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        
        user_question = st.text_input("Consult EduMind AI about this document:", placeholder="Type your query here...")
        
        if user_question:
            with st.spinner("EduMind AI is formulating a response..."):
                retrieved_docs = retriever.invoke(user_question)
                context = "\n\n".join([doc.page_content for doc in retrieved_docs])
                
                prompt = f"""أنت مساعد أكاديمي باللغة العربية ومهندس ذكاء اصطناعي عبقري. بناءً على النصوص المأخوذة من الكتاب المرفق، أجب على السؤال بكل دقة وبأسلوب مشوق ومنظم.
                ملاحظة هامة: رموز المعادلات الرياضية والتكاملات قد تظهر مشوهة برمجياً (مثل قراءة الرموز كأرقام مدمجة مثل 55). استخدم ذكاءك الرياضي لإصلاح سياق المعادلة والوصول للناتج النهائي الصحيح في صفحة الشرح.
                إذا لم تجد الإجابة في النص، قل 'المعلومة غير موجودة في الكتاب' ولا تقم بالتأليف.
                
                النصوص المتاحة من الكتاب:
                {{context}}
                
                السؤال الحالي: {{user_question}}"""
                
                formatted_prompt = prompt.format(context=context, user_question=user_question)
                
                response = ollama.chat(model='llama3', messages=[
                    {'role': 'user', 'content': formatted_prompt}
                ])
                
                st.markdown("### 🤖 RESPONSE:")
                # إظهار الإجابة بنص أزرق سماوي مضيء داخل إطار منسق وثابت
                st.markdown(f'''
                    <div style="background-color: #2D1A1A; border: 2px solid #5A2B2B; border-radius: 12px; padding: 20px; margin-top: 15px;">
                        <p style="color: #4BADFF; font-size: 1.15rem; line-height: 1.8; font-weight: 600; margin: 0;">{response["message"]["content"]}</p>
                    </div>
                ''', unsafe_allow_html=True)
    else:
        st.info("💡 Understated luxury is privacy. Upload a document on the left to initiate the AI.")
